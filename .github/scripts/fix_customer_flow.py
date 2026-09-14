from pathlib import Path
import re

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
            elif c==q: q=None
        else:
            if c in "'\"`": q=c
            elif c=='{': depth+=1
            elif c=='}':
                depth-=1
                if depth==0: return src[:start]+replacement+src[i+1:]
    raise RuntimeError(name+' closing brace not found')

p=Path('index.html'); src=p.read_text(encoding='utf-8')
new_submit="""  doSubmitSampleRequest(items, sess) {
    if (!sess || !sess.access_token || !items || !items.length) {
      this.setState({ sampleReqBusy: false, sampleReqSent: false, sampleReqError: 'Numune talebi oluşturulamadı. Tekrar deneyin.' });
      return;
    }
    this.setState({ sampleReqBusy: true, sampleReqSent: false, sampleReqError: '' });
    this.mergeGuestSamplesToAccount(sess).catch(() => null).then(() =>
      sbRest('/sample_requests', { method: 'POST', headers: { Prefer: 'return=representation' }, body: JSON.stringify({ user_id: sess.user.id }) }, sess.access_token)
    ).then((res) => {
      const req = res.ok && res.data && res.data[0];
      if (!req) throw new Error('sample request insert failed');
      return sbRest('/sample_request_items', { method: 'POST', headers: { Prefer: 'return=minimal' }, body: JSON.stringify(items.map((it) => Object.assign({ request_id: req.id }, it))) }, sess.access_token);
    }).then((itemRes) => {
      if (!itemRes || !itemRes.ok) throw new Error('sample request items insert failed');
      this.setState({ sampleReqBusy: false, sampleReqSent: true, sampleReqError: '' });
      setTimeout(() => {
        try { localStorage.removeItem('ah_samples'); } catch (e) {}
        this.setState({ samples: [], samplesOpen: false, sampleReqSent: false, rbStep: 0, rb: { group: 'Textured', colour: 'Beige', size: '160x230', use: 'Retail floor' } });
      }, 2200);
    }).catch(() => this.setState({ sampleReqBusy: false, sampleReqSent: false, sampleReqError: 'Bir hata oluştu, tekrar deneyin.' }));
  }"""
src=replace_method(src,'doSubmitSampleRequest',new_submit)
src=src.replace("samplesSendAll: 'Email this list'","samplesSendAll: 'Request selected samples'")
src=src.replace("samplesSendAll: 'Bu listeyi e-postayla gönder'","samplesSendAll: 'Seçili numuneleri talep et'")
src=src.replace('{{ t.samplesSendAll }} <span aria-hidden="true">→</span>','{{ samplesSendAllLabel }} <span aria-hidden="true">→</span>')
src=src.replace('{{ t.rbSendRequest }} <span aria-hidden="true">→</span>','{{ rbSendRequestLabel }} <span aria-hidden="true">→</span>')
if 'samplesSendAllLabel:' not in src:
    src=src.replace('samplesSendAll,\n      requestSamplesHandler:', "samplesSendAll,\n      samplesSendAllLabel: t.samplesSendAll + ((s.samples || []).length ? ' (' + (s.samples || []).length + ')' : ''),\n      requestSamplesHandler:")
if 'rbSendRequestLabel:' not in src:
    src=src.replace('rbCanContinue,', "rbCanContinue, rbSendRequestLabel: t.rbSendRequest + ((s.samples || []).length ? ' (' + (s.samples || []).length + ')' : ''),")
if 'sampleReqSubmitDisabled:' not in src:
    src=src.replace('sampleReqBusy: s.sampleReqBusy,', 'sampleReqBusy: s.sampleReqBusy, sampleReqSubmitDisabled: !!(s.sampleReqBusy || s.sampleReqSent),')
src=src.replace('disabled="{{ sampleReqBusy }}"','disabled="{{ sampleReqSubmitDisabled }}"')
if 'toggleAccountFn' not in src:
    src=src.replace("openLoginFn: () => this.openAuthModal('login'),", "accountOpen: s.accountOpen, toggleAccountFn: () => this.setState((p) => ({ accountOpen: !p.accountOpen })), closeAccountFn: () => this.setState({ accountOpen: false }), openLoginFn: () => this.openAuthModal('login'),")
pat=re.compile(r'<sc-if value="\{\{ isAuthed \}\}" hint-placeholder-val="\{\{ false \}\}">\s*<div style="\{\{ authPillStyle \}\}">\s*<a href="Hesabim\.dc\.html" style="\{\{ signInLinkStyle \}\}">(.*?)</a>\s*</div>\s*</sc-if>',re.S)
m=pat.search(src)
if m:
    inner=m.group(1)
    repl='''<sc-if value="{{ isAuthed }}" hint-placeholder-val="{{ false }}"><div style="position:relative;display:flex;align-items:center"><button type="button" onClick="{{ toggleAccountFn }}" aria-expanded="{{ accountOpen }}" style="{{ signInLinkStyle }}">'''+inner+'''</button><sc-if value="{{ accountOpen }}" hint-placeholder-val="{{ false }}"><div style="position:absolute;right:0;top:calc(100% + 10px);z-index:90;width:210px;padding:8px;background:#fbf5ee;border:1px solid rgba(76,38,15,.14);border-radius:14px;box-shadow:0 24px 50px -28px rgba(34,28,24,.55);display:flex;flex-direction:column"><a href="Hesabim.dc.html" style="padding:11px 12px;color:#221c18;text-decoration:none;font:500 13px/1.2 'DM Sans',sans-serif">{{ t.myAccount }}</a><a href="Hesabim.dc.html#samples" style="padding:11px 12px;color:#221c18;text-decoration:none;font:500 13px/1.2 'DM Sans',sans-serif">{{ t.acctStatSamples }}</a><a href="Hesabim.dc.html#requests" style="padding:11px 12px;color:#221c18;text-decoration:none;font:500 13px/1.2 'DM Sans',sans-serif">{{ t.acctStatRequests }}</a><button type="button" onClick="{{ logoutFn }}" style="padding:11px 12px;border:0;border-top:1px solid rgba(76,38,15,.10);background:none;text-align:left;color:#a5342f;font:600 12px/1.2 'DM Sans',sans-serif;cursor:pointer">{{ t.signOut }}</button></div></sc-if></div></sc-if>'''
    src=src[:m.start()]+repl+src[m.end():]
p.write_text(src,encoding='utf-8')

p=Path('Hesabim.dc.html'); src=p.read_text(encoding='utf-8')
new_save=""" saveProfile(){const sess=this._authSession();if(!sess||!sess.access_token)return;const f=this.state.profileForm;this.setState({profileSaving:true,profileError:'',profileSaved:false});sbRest('/profiles?id=eq.'+sess.user.id,{method:'PATCH',headers:{Prefer:'return=representation'},body:JSON.stringify({full_name:f.fullName||null,company:f.companyName||null,phone:f.phone||null,address:f.address||null})},sess.access_token).then((res)=>{const row=res.ok&&res.data&&res.data[0];if(!row){this.setState({profileSaving:false,profileError:this.state.lang==='tr'?'Kaydedilemedi. Tekrar deneyin.':'Could not save. Try again.'});return;}this.setState({profileSaving:false,profileSaved:true,profileError:''});}).catch(()=>this.setState({profileSaving:false,profileSaved:false,profileError:this.state.lang==='tr'?'Kaydedilemedi. Tekrar deneyin.':'Could not save. Try again.'}));}"""
src=replace_method(src,'saveProfile',new_save)
if "window.location.hash" not in src:
    src=src.replace("componentDidMount(){", "componentDidMount(){try{const tab=(window.location.hash||'').replace('#','');if(['samples','requests','company'].includes(tab))this.setState({accountTab:tab});}catch(e){}")
src=src.replace('disabled="{{ sampleReqBusy }}" class="primary-btn"','disabled="{{ sampleReqSubmitDisabled }}" class="primary-btn"')
if 'sampleReqSubmitDisabled:' not in src:
    src=src.replace('sampleReqBusy:s.sampleReqBusy,', 'sampleReqBusy:s.sampleReqBusy,sampleReqSubmitDisabled:!!(s.sampleReqBusy||s.sampleReqSent),')
p.write_text(src,encoding='utf-8')

p=Path('Admin.dc.html'); src=p.read_text(encoding='utf-8')
src=src.replace('/contact_requests?select=id,name,company,email,phone,country,message,created_at&order=created_at.desc','/contact_requests?select=id,name,company,email,phone,country,customer_type,message,consent,status,created_at&order=created_at.desc')
src=src.replace("country:r.country||'',message:r.message||''", "country:r.country||'',customerType:r.customer_type||'',consent:!!r.consent,status:r.status||'new',message:r.message||''")
src=src.replace('<sc-if value="{{ r.country }}" hint-placeholder-val="{{ false }}">· {{ r.country }}</sc-if></p>', '<sc-if value="{{ r.country }}" hint-placeholder-val="{{ false }}">· {{ r.country }}</sc-if><sc-if value="{{ r.customerType }}" hint-placeholder-val="{{ false }}"> · {{ r.customerType }}</sc-if></p>')
p.write_text(src,encoding='utf-8')

idx=Path('index.html').read_text(encoding='utf-8'); acc=Path('Hesabim.dc.html').read_text(encoding='utf-8'); adm=Path('Admin.dc.html').read_text(encoding='utf-8')
assert "request_id: req.id" in idx and "list_id: list.id" in idx
assert "res.ok && res.data && res.data[0]" in idx
assert "localStorage.removeItem('ah_samples')" in idx
assert 'toggleAccountFn' in idx and 'Hesabim.dc.html#samples' in idx and 'Hesabim.dc.html#requests' in idx
assert "Request selected samples" in idx and "Seçili numuneleri talep et" in idx
assert "method:'PATCH'" in acc and "/profiles?id=eq." in acc
assert "sampleReqSubmitDisabled" in idx and "sampleReqSubmitDisabled" in acc
assert 'customer_type' in adm and '{{ r.customerType }}' in adm
assert 'sample_request_id:' not in idx+acc and 'sample_list_id:' not in idx+acc
print('CUSTOMER_FLOW_REGRESSION_ASSERTIONS_PASS')