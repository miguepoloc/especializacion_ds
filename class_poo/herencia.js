class Invoice {
  constructor(id, amount) {
    this.id = id;
    this.amount = amount;
  }

  calculateTotal() {
    return this.amount;
  }
}

class TaxedInvoice extends Invoice {
  constructor(id, amount, tax) {
    super(id, amount);
    this.tax = tax;
  }

  calculateTotal() {
    const subtotal = super.calculateTotal();
    const tax = subtotal * (this.tax / 100);
    return subtotal + tax;
  }
}

class DiscountedInvoice extends Invoice {
  constructor(id, amount, discount) {
    super(id, amount);
    this.discount = discount;
  }

  calculateTotal() {
    const subtotal = super.calculateTotal();
    const discount = subtotal * (this.discount / 100);
    return subtotal - discount;
  }
}

const invoice1 = new TaxedInvoice(1, 100, 10);
console.log("Total gravado:", invoice1.calculateTotal());

const invoice2 = new DiscountedInvoice(2, 200, 20);
console.log("Total con descuento:", invoice2.calculateTotal());
