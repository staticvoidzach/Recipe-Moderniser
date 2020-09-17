<template>
    <!-- START INGREDIENT FIELD -->
    <div class="mt-3">
        <b-input-group>
            <b-input-group-prepend>
                <!-- START INGREDIENT QUANTITY INPUT -->
                <b-form-input v-model="quantity" @change="emitChange" id="quantity" type="number"></b-form-input>
                <!-- END INGREDIENT QUANTITY INPUT -->
                <!-- START INGREDIENT UNIT INPUT -->
                <b-form-select v-model="unit" @change="emitChange" id="unit"
                               :options="unitOptions"></b-form-select>
                <!-- END INGREDIENT UNIT INPUT -->
            </b-input-group-prepend>
            <!-- START INGREDIENT NAME INPUT -->
            <b-form-input @change="emitChange" v-model="name" :state="isValidIngredient"></b-form-input>
            <b-form-invalid-feedback id="inputLiveFeedback">
                {{ invalidMessage }}
            </b-form-invalid-feedback>
            <!-- END INGREDIENT NAME INPUT -->
        </b-input-group>
    </div>
    <!-- END INGREDIENT FIELD -->
</template>

<script>
    import { Ingredient } from "@/ingredient";

    export default {
        name: "IngredientField",
        props: [
            'index',
            'weightUnits',
            'baseWeightUnit',
            'volumeUnits',
            'baseVolumeUnit'

        ],
        data() {
            return {
                quantity: "", // Quantity of ingredient entered by user
                unit: null, // Unit of ingredient entered by user
                name: "", // Name of ingredient entered by user
            }
        },
        computed: {
            isValidIngredient() {
                let ingredient = new Ingredient(this.$data)

                if (ingredient.isEmpty()) {
                    return null
                }

                return ingredient.isFull() ? null : false
            },
            invalidMessage() {
              if (this.isValidIngredient === null) {
                  return ''
              }

              return "Please enter a" + (this.name === "" ? " name " : " quantity ") + "for this ingredient."

            },
            unitOptions() {
                // Create a list of order units that the user can select

                let options = [
                    {
                        value: null,
                        text: ""
                    }
                ]

                let skip = false
                for (const wuI in this.weightUnits) {
                    const wu = this.weightUnits[wuI] // Get the current weight unit

                    // If the current weight unit is less than the base weight unit or the base weight unit has already been found
                    if (wu.factor < 1 || skip) {
                        options.push(this.unitToOption(wu))
                        continue
                    }

                    // Weight unit is greater than base unit, so add base unit first
                    options.push(this.unitToOption(this.baseWeightUnit))

                    // Define that the base unit has already been added and shouldn't be added again
                    skip = true

                    // Add unit
                    options.push(this.unitToOption(wu))

                }

                skip = false
                for (const vuI in this.volumeUnits) {
                    const vu = this.volumeUnits[vuI] // Get the current volume unit

                    // If the current volume unit is less than the base volume unit or the base volume unit has already been found
                    if (vu.factor < 1 || skip) {
                        options.push(this.unitToOption(vu))
                        continue
                    }

                    // Volume unit is greater than base unit, so add base unit first
                    options.push(this.unitToOption(this.baseVolumeUnit))

                    // Define that the base unit has already been added and shouldn't be added again
                    skip = true

                    // Add unit
                    options.push(this.unitToOption(vu))

                }

                return options
            }
        },
        methods: {
            emitChange() {
                this.$emit('change',
                    this.index,
                    new Ingredient({name: this.name, quantity: this.quantity, unit: this.unit}))
            },
            unitToOption(unit) {
                return {
                    value: unit,
                    text: unit.name
                }
            },
        }
    }
</script>

<style scoped lang="scss">
    #quantity {
        border-top-right-radius: 0;
        border-bottom-right-radius: 0;
        width: 80px;
    }

    #unit {
        border-radius: 0;
    }

</style>