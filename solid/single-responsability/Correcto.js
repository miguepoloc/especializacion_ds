class Invoice {
    constructor(number, balance, amount, invoiceDate) {
        this.id = this.generateUniqueId();
        this.number = number;
        this.balance = balance;
        this.amount = amount;
        this.invoiceDate = invoiceDate;
    }

    generateUniqueId() {
        return Math.floor(Math.random() * 1000000000);
    }

    calculateTax(taxRate = 0.19) {
        return this.amount * (1 + taxRate);
    }

    print() {
        console.log("Invoice #" + this.number);
        console.log("Amount: " + this.amount);
        console.log("Balance: " + this.balance);
        console.log("Invoice Date: " + this.invoiceDate);
        console.log("Tax Amount : " + this.calculateTax(0.21));
    }
}

// Example usage:
const invoice = new Invoice("001", 2500, 5000, new Date())

invoice.print()