from pratclass import Filme, MaquinaDoTempo

filme_after = Filme("9:30", "After", "16", "136 min")

maquina_do_tempo_futuro = MaquinaDoTempo ("2070", "2025", "Italia", "Roma")

print(maquina_do_tempo_futuro.is_on)
print(filme_after.is_public)

filme_after.is_public = True
maquina_do_tempo_futuro .is_on = True

print(maquina_do_tempo_futuro.is_on)
print(filme_after.is_public)