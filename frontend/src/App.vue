<template>
    <div class="b-container" id="app">
        <b-jumbotron class="text-center" header="Recipe Moderniser" id="jumbotron"
                     lead="Modernise your recipes to make them easier to make!"></b-jumbotron>
        <b-row class="text-center">
            <b-col></b-col>
            <b-col cols="6">
                <!-- START SERVINGS COMPONENT -->
                <h3>Servings</h3>
                <b-alert v-model="showLargeAlert" variant="warning">Your scale factor is quite <strong>large</strong>!
                    Consider making smaller batches.
                </b-alert>
                <b-alert v-model="showSmallAlert" variant="warning">Your scale factor is quite <strong>small</strong>!
                    Consider making larger batches and freezing the leftovers.
                </b-alert>
                <!-- START RECIPE SERVINGS INPUT -->
                <b-input-group class="mb-2" prepend="Recipe Servings">
                    <b-form-input @blur="recalculateScaleFactor" v-model="recipeScale" type="number"></b-form-input>
                </b-input-group>
                <!-- END RECIPE SERVINGS INPUT -->
                <!-- START DESIRED SERVINGS INPUT -->
                <b-input-group class="mb-5" prepend="Desired Servings">
                    <b-form-input @blur="recalculateScaleFactor" v-model="desiredScale" type="number"></b-form-input>
                </b-input-group>
                <!-- END DESIRED SERVINGS INPUT -->
                <!-- END SERVINGS COMPONENT -->

                <!-- START INGREDIENTS INPUT COMPONENT -->
                <div v-if="scaleFactor != null">
                    <h3>Ingredients</h3>
                    <div v-if="!$apollo.loading" class="mb-5">
                        <IngredientField v-for="(ingredient, counter) in ingredients" :index="counter" :key="counter"
                                         @change="ingredientUpdated"
                                         :weight-units="weightUnits"
                                         :base-weight-unit="baseWeightUnit"
                                         :volume-units="volumeUnits"
                                         :base-volume-unit="baseVolumeUnit"></IngredientField>
                    </div>
                </div>
                <!-- END INGREDIENTS INPUT COMPONENT -->

                <!-- START NEW RECIPE INPUT COMPONENT -->
                <div v-if="scaleFactor != null && validIngredients.length > 0">
                    <h3>New Recipe</h3>
                    <ul class="mt-2 text-left">
                        <li
                                is="ModernisedIngredient"
                                v-for="(ingredient, index) in validIngredients"
                                :key="index"
                                :ingredient="ingredient"
                                :base-unit="getBaseUnit(ingredient)"
                                :scale-factor="scaleFactor"
                        ></li>
                    </ul>
                </div>
                <!-- END NEW RECIPE INPUT COMPONENT -->
            </b-col>
            <b-col></b-col>
        </b-row>
    </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import gql from 'graphql-tag'
import IngredientField from "./components/IngredientField";
import { Ingredient } from './ingredient'
import ModernisedIngredient from "./components/ModernisedIngredient";

export default {
    name: 'App',
    components: {ModernisedIngredient, IngredientField},
    data() {
        return {
            recipeScale: null, // Amount of servings the recipe makes my default (entered by user)
            desiredScale: null, // Amount of servings the user wants (entered by user)
            scaleFactor: null, // Calculated when desired scale and recipe scale are both valid
            weightUnits: null, // Units for weight - FETCHED BY GQL
            baseWeightUnit: null, // Base unit for weight - FETCHED BY GQL
            volumeUnits: null, // Units for volume - FETCHED BY GQL
            baseVolumeUnit: null, // Base unit for volume - FETCHED BY GQL
            ingredients: [
                new Ingredient({})
            ] // Ingredients entered by the user
        }
    },
    computed: {
        showLargeAlert() {
            // If the scale factor hasn't been / can't be calculated
            if (this.scaleFactor === null) {
                return false // Don't show alert
            }

            // Show if the scale factor is larger than 3
            return this.scaleFactor > 3
        },
        showSmallAlert() {
            // If the scale factor hasn't been / can't be calculated
            if (this.scaleFactor === null) {
                return false // Don't show alert
            }

            // Show if the scale factor is less than a quarter (0.25)
            return this.scaleFactor < 0.25
        },
        validIngredients() {
            // Return a filtered version of this.ingredients that only contains ingredients that have an amount and a name
            return this.ingredients.filter((el) => {
                return el.isFull() // && el.unit != null
            })
        }
    },
    methods: {
        getBaseUnit(ingredient) {
            if (ingredient.unit == null) {
                return null;

            // If the base unit name contains "WeightType"
            } else if (ingredient.unit.__typename.indexOf('WeightType') > -1) {
                return this.baseWeightUnit
            } else {
                return this.baseVolumeUnit
            }
        },
        ingredientUpdated(index, ingredient) {
            // Insert ingredient at index
            this.ingredients.splice(index, 1, ingredient)

            // If is last ingredient
            if ((this.ingredients.length - 1) === index) {
                if (!ingredient.isEmpty()) {
                    this.ingredients.push(new Ingredient({}))
                    // If this and above is empty
                } else if (this.ingredients.length > 1 &&
                    this.ingredients[this.ingredients.length - 2].isEmpty()) {
                    this.ingredients.pop()
                }
                // If is second to last ingredient
            } else if ((this.ingredients.length - 2) === index) {
                // If both 2nd to last and last are empty
                if (ingredient.isEmpty() && this.ingredients[this.ingredients.length - 1].isEmpty()) {
                    this.ingredients.pop()
                }
            }
        },
        recalculateScaleFactor() {
            // If either the desired scale or recipe scale is invalid then the scale factor is null
            if (!this.desiredScale || !this.recipeScale) {
                this.scaleFactor = null
                return
            }

            // Calculate and assign scale factor
            this.scaleFactor = this.desiredScale / this.recipeScale
        }
    },
    apollo: {
        weightUnits: gql`
                query {
                    weightUnits: allWeightUnits {
                        name,
                        factor
                    }
                }
            `,
        volumeUnits: gql`
                query {
                    volumeUnits: allVolumeUnits {
                        name,
                        factor
                    }
                }
            `,
        baseWeightUnit: gql`
                query {
                    baseWeightUnit {
                        name,
                    }
                }
            `,
        baseVolumeUnit: gql`
                query {
                    baseVolumeUnit {
                        name,
                    }
                }
            `
    }
}
</script>

<style lang="scss">
$primary: lightcoral;

#app {
  margin-bottom: 8rem;
}

.input-group-text {
  width: 150px;
  background: $primary;
  color: white;
  border: none;
}

#jumbotron {
  background: $primary;
  color: white;
  border-radius: 0;
}

h3 {
  color: $primary;
}
</style>
