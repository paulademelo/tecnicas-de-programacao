from factory.calculate__pib_per_capta_factory import CalculatePibFactory

# Refatoração:
# 1. Verificar métodos com nomes significativos
# 2. Padronizar nomes de métodos com o snake_pattern
# 3. Remover código hard-coded
# 4. Padronizar a estrutura do código com identação
# 5. Padronizar constantes e variáveis
# 6. Padronizar e organizar blocos com responsabilidades semelhantes

def main():

    calculate = CalculatePibFactory.create_instance()
    
    print(calculate)
    calculate.load_file()
    calculate.load_uf_by_region()
    calculate.print_all_content() 
    calculate.get_state_by_region('CO')
    calculate.get_region_by_state('Sao Paulo')
main()