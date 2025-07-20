import json
from glob import glob

MEDICOES = sorted(glob("medicoes/*.json"))
print(MEDICOES)



def open_file(file_path: list[str]):
    
    for med in file_path:
        json_correct = []
        with open(med) as f:
            for line in f:
                l = json.loads(line)
                json_correct.append(l)
                print(json_correct)
        
        with open(f"correct_{med.split("/")[-1]}","w") as f:
            json.dump(json_correct,f,indent=2)
    ...
    

if __name__ == "__main__":
    open_file(MEDICOES)