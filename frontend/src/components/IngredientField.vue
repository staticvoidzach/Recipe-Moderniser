<template>
    <div class="mt-3">
        <b-input-group>
            <b-input-group-prepend>
                <b-form-input v-model="quantity" @change="emitChange" id="quantity" type="number"></b-form-input>
                <b-form-select v-model="unit" @change="emitChange" id="unit"
                               :options="[{'value': {'name': 'One', 'factor': 1}, 'text': 1}, {'value': {'name': 'Two', 'factor': 2}, 'text': 2}]"></b-form-select>
            </b-input-group-prepend>
            <b-form-input @change="emitChange" v-model="name"></b-form-input>
        </b-input-group>
    </div>
</template>

<script>
    import { Ingredient } from "../ingredient";

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
                quantity: "",
                unit: null,
                name: "",
            }
        },
        methods: {
            emitChange() {
                this.$emit('change',
                    this.index,
                    new Ingredient({name: this.name, quantity: this.quantity, unit: this.unit}))
            }
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