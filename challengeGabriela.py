'''
Funcție care calculeaza un discount:
- printezi pe ecran: 'discountul calculat e de 5%'
- apoi trimiți discountul spre exterior ca să îl aplici la calculul prețului

Că sa facem treaba treabă ține cont că trebuie să
- ai și taxă de shipping de 5 dolari
- taxă de handling de 2 dolari
- calculează valoarea totală a comenzii tinând cont de discountul calculat ca procentaj din preț,  taxa de shipping și taxa de handling
'''

class discount_challenge():
    pret=0
    taxa_shipping=0
    taxa_handling=0

    def __init__(self, pret, shipping, handling):
        self.pret=pret
        self.taxa_shipping=shipping
        self.taxa_handling=handling

    def discount(self, procent_discount):
        disc_procentual=self.pret*procent_discount/100
        pret_dupa_discount=self.pret-disc_procentual+self.taxa_handling+self.taxa_shipping
        print(f'Discount-ul aplicat este de {disc_procentual} USD')
        return f'Pretul produsului dupa aplicarea discountului este de {pret_dupa_discount} USD'

discount5=discount_challenge(100,5,2)
print(discount5.discount(5))







