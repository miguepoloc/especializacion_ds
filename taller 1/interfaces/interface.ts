abstract class AbstrabWatch {
    brand: string;
    model: string;
    price: number;
    isOn: boolean = false;

    constructor(brand: string, model: string, price: number) {
        this.brand = brand;
        this.model = model;
        this.price = price;
    }

    abstract setTime(time: string): void;

    abstract turnOn(): void 

    abstract turnOff(): void;    

}

class SmartWatchA extends AbstrabWatch {
    setTime(time: string): void {
        if (this.isOn) {
            console.log(`${this.brand} ${this.model} - Time set to ${time}`);
        } else {
            console.log(`${this.brand} ${this.model} is turned off.`);
        }
    }
    turnOn(): void {
        this.isOn = true;
        console.log(`${this.brand} ${this.model} - Turned on.`);
    }
    turnOff(): void {
        this.isOn = false;
        console.log(`${this.brand} ${this.model} - Turned off.`);
    }
    batteryLevel: number = 100;

    constructor(brand: string, model: string, price: number) {
        super(brand, model, price);
    }

    additionalFunctionality(): void {
        console.log(`${this.brand} ${this.model} - Battery level: ${this.batteryLevel}%`);
    }

    chargeBattery(): void {
        console.log(`${this.brand} ${this.model} - Charging...`);
        this.batteryLevel = 100;
        console.log(`${this.brand} ${this.model} - Battery fully charged.`);
    }
}

class ClassicWatchA extends AbstrabWatch {
    setTime(time: string): void {
            if (this.isOn) {
            console.log(`${this.brand} ${this.model} - Time set to ${time}`);
        } else {
            console.log(`${this.brand} ${this.model} is turned off.`);
        }
    }
    turnOn(): void {
        this.isOn = true;
        console.log(`${this.brand} ${this.model} - Turned on.`);
    }
    turnOff(): void {
        this.isOn = false;
        console.log(`${this.brand} ${this.model} - Turned off.`);
    }
    style: string;

    constructor(brand: string, model: string, price: number, style: string) {
        super(brand, model, price);
        this.style = style;
    }
}


const smartwatch1 = new SmartWatchA("Apple", "Watch Series 6", 399);
smartwatch1.turnOn();
smartwatch1.setTime("10:30 AM");
smartwatch1.chargeBattery();
smartwatch1.turnOff();

const classicWatch2 = new ClassicWatchA("Rolex", "Submariner", 10000, "Luxury");
classicWatch2.turnOn();
classicWatch2.setTime("10:30 AM");
classicWatch2.turnOff();
