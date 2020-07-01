<template>
    <div class="b-container" id="app">
        <b-jumbotron class="text-center" header="Recipe Moderniser"
                     lead="Modernise your recipes to make them easier to make!"></b-jumbotron>
        <b-row class="text-center">
            <b-col></b-col>
            <b-col cols="6">
                <h3>Servings</h3>
                <b-alert v-model="showLargeAlert" variant="warning">Your scale factor is quite <strong>large</strong>! Consider making smaller batches.</b-alert>
                <b-alert v-model="showSmallAlert" variant="warning">Your scale factor is quite <strong>small</strong>! Consider making larger batches and freezing the leftovers.</b-alert>
                <b-input-group class="mb-2" prepend="Recipe Servings">
                    <b-form-input v-model="recipeScale" type="number"></b-form-input>
                </b-input-group>
                <b-input-group class="mb-5" prepend="Desired Servings">
                    <b-form-input v-model="desiredScale" type="number"></b-form-input>
                </b-input-group>
                <h3>Ingredients</h3>
                <IngredientField v-for="(ingredient, counter) in ingredients" :index="counter" :key="counter" @change="ingredientUpdated"></IngredientField>
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

    export default {
        name: 'App',
        components: {IngredientField},
        data() {
            return {
                recipeScale: null,
                desiredScale: null,
                weightUnits: null,
                baseWeightUnit: null,
                volumeUnits: null,
                baseVolumeUnit: null,
                ingredients: [
                    new Ingredient({})
                ]
            }
        },
        computed: {
            scaleFactor() {
                if (!this.desiredScale || !this.recipeScale) {
                    return null
                }
                return this.desiredScale / this.recipeScale
            },
            showLargeAlert() {
                if (this.scaleFactor === null) {
                    return false
                }
                return this.scaleFactor > 3
            },
            showSmallAlert() {
                if (this.scaleFactor === null) {
                    return false
                }
                return this.scaleFactor < 0.25
            },
        },
        methods: {
            ingredientUpdated(index, ingredient) {
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

</style>
