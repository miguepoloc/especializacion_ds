class Invoice {
  #numeration = "";
  #date = new Date();
  #client = "";
  #products = [];
  #seller = "";

  constructor(cli, seller) {
    this.#client = cli;
    this.#date = new Date();
    this.#numeration = Math.round(Math.random() * 100);
    this.#seller = seller;
  }

  getNumber() {
    return this.#numeration;
  }

  getClient() {
    return this.#client;
  }

  getProducts() {
    return this.#products
      .map((e) => `${e.prod} - $${e.unitPrice} x ${e.quantity}`)
      .join("\n\t");
  }

  getSeller() {
    return this.#seller;
  }

  addProduct(prod, quantity, unitPrice) {
    this.#products.push({ prod, quantity, unitPrice });
  }

  formatDate() {
    const monthNames = [
      "enero",
      "febrero",
      "marzo",
      "abril",
      "mayo",
      "junio",
      "julio",
      "agosto",
      "septiembre",
      "octubre",
      "noviembre",
      "diciembre",
    ];

    // Obtener componentes de la fecha
    const day = String(this.#date.getDate()).padStart(2, "0");
    const monthIndex = this.#date.getMonth();
    const year = this.#date.getFullYear();

    // Formatear la fecha en formato dd de mes yyyy
    return `${day} de ${monthNames[monthIndex]} ${year}`;
  }

  #deleteProductFromList(prod) {
    this.#products = this.#products.filter((pr) => pr.prod !== prod);
  }

  removeProduct(prod) {
    const p = this.#products.find((p) => p.prod === prod);

    if (p && p.quantity > 0) {
      p.quantity -= 1;

      if (p.quantity === 0) {
        this.#deleteProductFromList(prod);
      }
    } else if (p && p.quantity === 0) {
      this.#deleteProductFromList(prod);
    } else {
      throw new Error("El producto no está en la factura");
    }
  }

  print() {
    console.log(`Factura N°${this.getNumber()}`);
    console.log("|---------------------|");
    console.log(`Cliente: ${this.getClient()}`);
    console.log(`Vendedor: ${this.getSeller()}`);
    console.log(`Productos:\n\t${this.getProducts()}`);
    console.log("|---------------------|");
    console.log(`Total: $${this.calculateTotal()}`);
    console.log(`Fecha: ${this.formatDate(this.#date)}`);
  }

  calculateTotal() {
    let total = 0;
    for (const item of this.#products) {
      total += item.unitPrice * item.quantity;
    }
    return total;
  }
}

const invoice = new Invoice("Pepito", "Juanito");

invoice.addProduct("Camiseta", 25000, 2);
invoice.addProduct("Pantalon", 14000, 3);

try {
  invoice.print();

  //deleteProductFromList es un método privado, por tanto no se puede usar
  invoice.#deleteProductFromList("Camiseta");
  invoice.print();
} catch (error) {
  console.log(error);
}
