class Category:
    def __init__(self, category, bal=0):
        self.category =category
        self.ledger = []
        self.balance = bal

    def __str__(self):
        # Format the title centered in a line of *'s
        title = self.category.center(30, '*') + '\n'
        
        # Format the ledger items
        items = ''
        for item in self.ledger:
            description = item['description'][:23]
            amount = f"{item['amount']:.2f}"[:7]
            items += f"{description:<23}{amount:>7}\n"
        
        # Add the total balance
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount':amount, 'description': description})
        self.balance += amount
    
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {destination.category}')
            destination.deposit(amount, f'Transfer from {self.category}')
            return True           
        else:
            return False

    def check_funds(self, amount):
        return True if self.get_balance() >= amount else False
        

def create_spend_chart(categories):
    
    spendings = []
    purpose = []
    for category in categories:
        spent = sum(-1 * entry['amount'] for entry in category.ledger if entry['amount'] < 0 )
        spendings.append(spent)
        purpose.append(category.category)
        
    total = sum(spendings)
    percentages = []
    for i in range(0,len(spendings)):
        percentage = int(spendings[i] / total * 100 // 10 * 10) if len(spendings) != 0 else 0
        percentages.append(percentage)

    chart_data =[]
    for i in range(len(percentages)):
        category = purpose[i]
        chart_data.append({'category':category, 'percentage':percentages[i]})

    output = 'Percentage spent by category\n'
    for i in range(100,-10,-10):
        out =  f'{i:>3}| '
        for j in range(len(chart_data)): 
            out += 'o  ' if i <= chart_data[j]['percentage'] else '   '
        output += out + '\n'
    output += '    '

    for _ in range(len(out)-4):
        output += '-'
    output += '\n     '

    max_length = 0
    for data in chart_data:
        max_length = len(data['category']) if len(data['category']) > max_length else max_length

    for i in range(max_length):
        for j in range(len(chart_data)):
            output += chart_data[j]['category'][i] + '  '  if i < len(chart_data[j]['category']) else '   '
        output += '\n     '
    output = output.rstrip('    ')
    
    return output.rstrip('\n')
                
            
