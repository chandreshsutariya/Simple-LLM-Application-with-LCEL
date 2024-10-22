from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8000/chain/")
description = remote_chain.invoke({"title": "Navaratri"})


print("\n",description,"\n")