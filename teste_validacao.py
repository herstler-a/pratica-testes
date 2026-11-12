from validacao import email_valido

def teste_email_correto_e_aceito();
  resultado = email_valido("ana@senac.br")
  assert resultado is True

def teste_email_sem_arroba_e_rejeitado():
  resultado = email_valido("anasenac.br")
  assert False, "complete este teste"

def teste_email_vazio_e_rejeitado():
  resultado = email_valido("")
  assert False, "complete este teste"
