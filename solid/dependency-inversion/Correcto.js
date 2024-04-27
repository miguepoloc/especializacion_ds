/**
 * POR EXTENSIÓN DEL CÓDIGO, SE ACORDÓ ENVIAR SOLO EL CASO CORRECTO DE LA INVERSIÓN DE DEPENDENCIAS
 */

//INTERFACES
class Invoice {
  constructor(number) {
    this.number = number;
  }

  print() {
    throw new Error("Method 'print' not implemented");
  }

  mapItems() {
    throw new Error("Method 'mapItems' not implemented");
  }

  calculateTotal() {
    throw new Error("Method 'calculateTotal' not implemented");
  }
}

class InvoicePrinter {
  print(invoice) {
    throw new Error("Method 'print' not implemented");
  }
}

//IMPLEMENTACIÓN DE CLASES
class SalesInvoice extends Invoice {
  constructor(number, seller, items) {
    super(number);
    this.seller = seller;
    this.items = items;
  }

  mapItems() {
    console.log("Items: ");
    this.items.forEach((e) => {
      console.log(
        `\t${e.product} x${e.quantity} ${e.price}c/u = ${e.price * e.quantity}`
      );
    });
  }

  calculateTotal() {
    return this.items.reduce((acc, cur) => {
      return acc + cur.quantity * cur.price;
    }, 0);
  }

  print() {
    console.log("===| Printing Sales Invoice |===");
    console.log("Number: ", this.number);
    console.log("Seller: ", this.seller);
    this.mapItems();
    console.log("Total: ", this.calculateTotal());
  }
}

class PurchaseInvoice extends Invoice {
  constructor(number, client, items) {
    super(number);
    this.client = client;
    this.items = items;
  }

  mapItems() {
    console.log("Items: ");
    this.items.forEach((e) => {
      console.log(
        `\t${e.product} x${e.quantity} ${e.price}c/u = ${e.price * e.quantity}`
      );
    });
  }

  calculateTotal() {
    return this.items.reduce((acc, cur) => {
      return acc + cur.quantity * cur.price;
    }, 0);
  }

  print() {
    console.log("===| Printing Purchase Invoice |===");
    console.log("Number: ", this.number);
    console.log("Client: ", this.client);
    this.mapItems();
    console.log("Total: ", this.calculateTotal());
  }
}

class ConsoleInvoicePrinter extends InvoicePrinter {
  print(invoice) {
    invoice.print();
  }
}

class PdfInvoicePrinter extends InvoicePrinter {
  print(invoice) {
    console.log("\n\nGenerating PDF for invoice:");
    invoice.print();
  }
}

const items = [
  { product: "Item 1", quantity: 3, price: 2500 },
  { product: "Item 2", quantity: 4, price: 1500 },
  { product: "Item 3", quantity: 10, price: 4333 },
];

const salesInvoice = new SalesInvoice("001", "Juanito Alimaña", items);
const purchaseInvoice = new PurchaseInvoice("002", "Pedro navaja", items);

const consolePrinter = new ConsoleInvoicePrinter();
const pdfPrinter = new PdfInvoicePrinter();

consolePrinter.print(salesInvoice);
consolePrinter.print(purchaseInvoice);

pdfPrinter.print(salesInvoice);
pdfPrinter.print(purchaseInvoice);
