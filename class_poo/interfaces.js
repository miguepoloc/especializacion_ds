class InterfaceMethods {
  print() {
    throw new Error('Method "print" not implemented.');
  }

  formatDate() {
    throw new Error("formatDate method must be implemented");
  }
}

class Invoice extends InterfaceMethods {
  numeration = "";
  date = new Date();
  client = "";
  products = [];
  seller = "";

  constructor(num, dat, cli, seller) {
    super();
    this.client = cli;
    this.date = dat;
    this.numeration = num;
    this.seller = seller;
  }

  getNumber() {
    return this.numeration;
  }

  getClient() {
    return this.client;
  }

  getProducts() {
    return this.products
      .map((e) => `${e.prod} - $${e.unitPrice} x ${e.quantity}`)
      .join("\n\t");
  }

  getSeller() {
    return this.seller;
  }

  addProduct(prod, quantity, unitPrice) {
    this.products.push({ prod, quantity, unitPrice });
  }

  #removeProduct(prod) {
    this.products = this.products.filter((pr) => pr.prod !== prod);
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
    const day = String(this.date.getDate()).padStart(2, "0");
    const monthIndex = this.date.getMonth();
    const year = this.date.getFullYear();

    // Formatear la fecha en formato dd de mes yyyy
    return `${day} de ${monthNames[monthIndex]} ${year}`;
  }

  removeProduct(prod) {
    const p = this.products.find((p) => p.prod === prod);

    if (p && p.quantity > 0) {
      p.quantity -= 1;

      if (p.quantity === 0) {
        this.#removeProduct(prod);
      }
    } else if (p && p.quantity === 0) {
      this.#removeProduct(prod);
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
    console.log(`Fecha: ${this.formatDate(this.date)}`);
  }

  calculateTotal() {
    let total = 0;
    for (const item of this.products) {
      total += item.unitPrice * item.quantity;
    }
    return total;
  }
}

class SupportTicket extends InterfaceMethods {
  ticketId = 0;
  content = "";
  status = "closed";
  date = new Date();

  constructor(content) {
    super();
    this.ticketId = Math.round(Math.random() * 1000);
    this.setContent(content);
    this.setStatus("open");
  }

  setContent(content) {
    this.content = content;
  }

  setStatus(status) {
    this.status = status === "open" ? "Abierto" : "Cerrado";
  }

  formatDate() {
    // Obtener componentes de la fecha
    const day = String(this.date.getDate()).padStart(2, "0");
    const month = String(this.date.getMonth() + 1).padStart(2, "0");
    const year = this.date.getFullYear();

    // Formatear la fecha en formato dd/mm/yyyy
    return `${day}/${month}/${year}`;
  }

  print() {
    console.log(`Ticket N°${this.ticketId}`);
    console.log("|---------------------|");
    console.log(`Mensaje: ${this.content}`);
    console.log(`Estado: ${this.status}`);
    console.log("|---------------------|");
    console.log(`Fecha: ${this.formatDate(this.date)}`);
  }
}

const invoice = new Invoice(1, new Date(), "Juan", "Pedro");

invoice.addProduct("Pizza", 2, 1500);
invoice.addProduct("Salchipapa", 16, 2600);

invoice.print();

console.log("\n\n\n\n");

const ticket = new SupportTicket("Lorem ipsum dolor sit amet spirit");

ticket.print();
