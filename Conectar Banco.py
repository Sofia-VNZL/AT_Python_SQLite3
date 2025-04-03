import sqlite3
from pathlib import path

DIR_CUR = Path(__file__).parent.resolve()
DB_NAME = 'mercado-at.db'
DB_FILE = DIR_CUR / DB_NAME

def conectar():
  try:
    conn = sqlite3.connect(DB_FILE)
    Print(f"Banco {DB_NAME} conetado com sucesso!")
  except Exception as e:
    print("Erro ao conectar o banco: {e}")
  return conn

  
  def desconectar(conn):
    try:
      if(conn):
        conn.close()
        Print(f"Conexão com banco {DB_NAME} fechada com sucesso")
    except Exception as e:
      Print(f"Erro ao fechar o banco: {e}")

  
  

  
  cursor = conn.cursor()



cursor.close()
conn.close() 
