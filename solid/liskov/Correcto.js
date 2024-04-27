class Invoice {
    constructor(number, amount) {
        this.number = number;
        this.amount = amount;
    }

    calculateTotal() {
        return this.amount;
    }

    toString() {
        return `Invoice ${this.number}: $${this.amount}`;
    }
}

class Discount extends Invoice {
    constructor(number, amount, discountPercentage) {
        super(number, amount);
        this.discountPercentage = discountPercentage;
    }

    calculateTotal() {
        const discountedAmount = this.amount - (this.amount * (this.discountPercentage / 100));
        return discountedAmount;
    }

    toString() {
        return `Discount ${this.number}: $${this.calculateTotal()} (Discount: ${this.discountPercentage}%)`;
    }
}

const invoice1 = new Invoice("001", 100);
console.log(invoice1.toString());

const invoice2 = new Discount("002", 200, 10);
console.log(invoice2.toString());

function printInvoiceTotal(invoice) {
    console.log(`Total: $${invoice.calculateTotal()}`);
}

printInvoiceTotal(invoice1);
printInvoiceTotal(invoice2);