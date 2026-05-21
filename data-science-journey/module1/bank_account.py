class BankAccount : 
    def __init__(self, name :str,balance = 0.0) -> None:
        self.name = name
        self.balance = balance
        self.history = []

    def deposit(self, amount :float) -> None:
        if amount <= 0 :
            raise ValueError(f"Impossible e déposé un montant négatif ou nul : {amount}")
        self.balance += amount

        self.history.append({
            "type" : "deposit",
            "amount" : amount,
            "balance_after" : self.balance
        })
    
    def withdraw(self, amount : float) -> None:
        if amount <= 0 :
            raise ValueError(f"Impossible de retirer un montant négatif ou nul : {amount}")
        if amount > self.balance :
            raise ValueError(f"gros bouffon tu n'as pas assez d'argent en banque (ton solde : {self.balance}) pour retirer : {amount} > ")
        self.balance -= amount
        
        self.history.append({
            "type" : "withdraw",
            "amount" : amount,
            "balance_after" : self.balance
        })

    


