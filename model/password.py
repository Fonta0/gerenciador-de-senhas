from datetime import datetime
from pathlib import Path

class ModeloBasico():
    base_dir = Path(__file__).resolve().parent.parent
    db_dir = base_dir / 'db'
    
    def save(self):
        table_path = Path(self.db_dir / f'{self.__class__.__name__}.txt')
        
        if not table_path.exists():
            table_path.touch()

        with open(table_path, 'a') as arq:
            arq.write("|".join(list(map(str, self.__dict__.values()))))
            arq.write('\n')
        
    @classmethod
    def get(cls):
        table_path = Path(cls.db_dir / f'{cls.__name__}.txt')
        
        if not table_path.exists():
            table_path.touch()
        
        with open(table_path, 'r') as arq:
            v = arq.readlines()
        
        results = []
        
        atributos = vars(cls())
        for i in v:
            split_w = i.split('|')
            tmp_dict = dict(zip(atributos, split_w))
            results.append(tmp_dict)
        
        return results


class Password(ModeloBasico):
    def __init__(self, domain=None, password=None, expire=False):
        self.domain = domain
        self.password = password
        self.create_at = datetime.now().isoformat()



