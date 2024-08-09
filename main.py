from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

with open('actions.json') as json_file:
    data = json.load(json_file)

def get_action_by_codeword(codeword: str):
    for action in data['actions']:
        if action['codeword'] == codeword:
            return action
    return None

def get_codewords_by_action_id(action_id):
    codewords = [action['codeword'] for action in data['actions'] if action['id'] == action_id]
    return codewords

@app.get("/action/{codeword}")
async def read_action(codeword: int):
    action_id = get_action_by_codeword(codeword)
    if action_id is None:
        raise HTTPException(status_code=404, detail="Codeword not found")
    return action_id

@app.get("/codewords/{action_id}")
async def read_codewords_by_action_id(action_id: str):
    codewords = get_codewords_by_action_id(action_id)
    if not codewords:
        raise HTTPException(status_code=404, detail="Action ID not found")
    return {"action_id": action_id, "codewords": codewords}