<template>
    <!-- START MODERNISED INGREDIENT -->
    <li>
        <strong>{{ amount }} {{ baseUnit != null ? baseUnit.name : ''}}</strong> <span id="spacer"></span> {{ ingredient.name }}
    </li>
    <!-- END MODERNISED INGREDIENT -->
</template>

<script>
    export default {
        name: "ModernisedIngredient",
        props: [
            'ingredient',
            'scaleFactor',
            'baseUnit',
        ],
        computed: {
            amount() {
                let factor = 1 // Default value if the unit factor cannot be found or the unit is the base unit

                // Try and find a unit factor
                if (this.ingredient.unit != null && 'factor' in this.ingredient.unit) {
                    factor = parseFloat(this.ingredient.unit.factor)
                }


                // Calculate the required quantity
                let quantity = parseFloat(this.ingredient.quantity) * factor * parseFloat(this.scaleFactor)

                // Make the quantity a 2 digit float
                quantity = quantity.toFixed(2)

                // If the quantity is a whole number, make quantity a whole number in a string, otherwise make it a .2 float
                quantity = Number.isInteger(parseFloat(quantity)) ? parseInt(quantity).toString() : quantity

                // If the last digit is 0 and the quantity not a whole number, remove the zero from the string, otherwise leave it.
                return quantity.substr(-1) === "0" && quantity.indexOf(".") > -1 ? quantity.substr(0, quantity.length - 1) : quantity
            }
        }
    }
</script>

<style scoped lang="scss">
#spacer {
  margin: 0 10px;
}
</style>