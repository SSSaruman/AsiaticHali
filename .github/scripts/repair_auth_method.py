from pathlib import Path
import re

p=Path('index.html')
src=p.read_text(encoding='utf-8')

def replace_method(src,name,replacement):
    m=re.search(r'(?m)^[ \t]+'+re.escape(name)+r'\([^)]*\)\s*\{',src)
    if not m: raise RuntimeError(name+' method definition not found')
    start=m.start(); brace=src.find('{',m.start(),m.end()+1)
    depth=0; q=None; esc=False
    for i in range(brace,len(src)):
        c=src[i]
        if q:
            if esc: esc=False
            elif c=='\\': esc=True
            elif c==q:q=None
        else:
            if c in "'\"`":q=c
            elif c=='{':depth+=1
            elif c=='}':
                depth-=1
                if depth==0:return src[:start]+replacement+src[i+1:]
    raise RuntimeError(name+' closing brace not found')

new_method="""  submitAuthForm() {
    const f = this.state.authForm;
    if (!f.email || !f.password) { this.setState({ authError: 'E-posta ve şifre gerekli.' }); return; }
    this.setState({ authBusy: true, authError: '' });
    const isRegister = this.state.authMode === 'register';
    const call = isRegister
      ? sbAuthFetch('/signup', { email: f.email, password: f.password, data: { full_name: f.fullName, company_name: f.companyName } })
      : sbAuthFetch('/token?grant_type=password', { email: f.email, password: f.password });
    call.then((res) => {
      if (isRegister && res.ok && res.data && res.data.user && !res.data.access_token) {
        this.setState({ authBusy: false, authFlowState: 'signup_success_pending_verification', pendingEmail: f.email });
        return;
      }
      if (!res.ok || !res.data || !res.data.access_token) {
        this.setState({ authBusy: false, authError: 'Giriş başarısız. Bilgilerinizi kontrol edin.' });
        return;
      }
      if (res.data.user && !res.data.user.email_confirmed_at) {
        try { localStorage.setItem('ah_auth', JSON.stringify({ access_token: res.data.access_token, refresh_token: res.data.refresh_token, user: res.data.user })); } catch (e) {}
        this.setState({ authBusy: false, authFlowState: 'login_unverified', pendingEmail: res.data.user.email });
        return;
      }
      const sess = { access_token: res.data.access_token, refresh_token: res.data.refresh_token, user: res.data.user };
      this._persistAuth(sess);
      if (isRegister) {
        sbRest('/profiles', {
          method: 'POST',
          headers: { Prefer: 'resolution=merge-duplicates,return=minimal' },
          body: JSON.stringify({ id: sess.user.id, full_name: f.fullName || null, company: f.companyName || null })
        }, sess.access_token);
      }
      const pending = this.state.authPendingAction;
      if (pending && pending.type === 'sampleRequest') this.doSubmitSampleRequest(pending.items, sess);
      this.setState({ authPendingAction: null });
    }).catch(() => this.setState({ authBusy: false, authError: 'Bir hata oluştu. Tekrar deneyin.' }));
  }"""

src=replace_method(src,'submitAuthForm',new_method)
p.write_text(src,encoding='utf-8')
print('AUTH_METHOD_REPAIRED')