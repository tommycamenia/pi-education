"""Local Worker checks only; synthetic identities and contact details."""
import json,uuid,urllib.request,urllib.error
BASE='http://127.0.0.1:5174';owner='chat-test-'+uuid.uuid4().hex;checks=0

def call(path='/api/chat',method='GET',body=None,user=owner,email='test@example.test',origin=BASE):
 h={'Origin':origin,'Content-Type':'application/json'}
 if user:h.update({'oai-authenticated-user-id':user,'oai-authenticated-user-email':email})
 try:
  r=urllib.request.urlopen(urllib.request.Request(BASE+path,data=json.dumps(body).encode() if body is not None else None,headers=h,method=method));return r.status,json.load(r)
 except urllib.error.HTTPError as e:return e.code,json.loads(e.read())
def expect(code,r):
 global checks
 assert r[0]==code,(code,r);checks+=1;return r[1]
expect(401,call(user=None));expect(403,call('/api/chat?admin=1'));expect(403,call('/api/chat?owner=another-user'))
b=dict(name='TEST PARENT',phone='080000000000',body='<script>test</script>',request_key=str(uuid.uuid4()))
expect(403,call(method='POST',body=b,origin='https://other.example'))
expect(400,call(method='POST',body={**b,'phone':'x'}));expect(400,call(method='POST',body={**b,'body':'a'*2001}))
id=expect(201,call(method='POST',body=b))['message']['id'];assert expect(200,call(method='POST',body=b))['message']['id']==id
rows=expect(200,call())['messages'];assert len(rows)==1 and rows[0]['body']==b['body']
assert expect(200,call(user='other-chat-test'))['messages']==[]
reply=dict(owner=owner,body='TEST SCHOOL REPLY',request_key=str(uuid.uuid4()))
expect(403,call(method='POST',body=reply));expect(201,call(method='POST',body=reply,user='local_seedy',email='seedy@sites.test'))
rows=expect(200,call())['messages'];assert len(rows)==2 and rows[1]['role']=='school'
threads=expect(200,call('/api/chat?admin=1',user='local_seedy',email='seedy@sites.test'))['threads'];assert any(t['owner']==owner for t in threads)
expect(200,call('/api/chat?owner='+owner,user='local_seedy',email='seedy@sites.test'))
print('Passed',checks,'chat checks: persistence, owner isolation, admin replies, idempotency, input limits and cross-origin protection.')
