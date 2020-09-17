class Ingredient {
    constructor({name = "", quantity = "", unit = null}) {
        this.name = name.trim();
        this.quantity = quantity.trim();
        this.unit = unit;
    }

    isEmpty() {
        return this.name === "" &&
            (this.quantity === "" || this.quantity === "0")
    }

    isFull() {
        return this.name !== "" &&
            (this.quantity !== "" && this.quantity !== "0")
    }
}

export { Ingredient }