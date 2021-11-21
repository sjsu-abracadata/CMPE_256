<template>
    <div>
        <b-form-datepicker class="mb-2" v-model="selectedDate" @input="selectedValue()"></b-form-datepicker>
    </div>
</template>

<script>
import moment from 'moment'
import eventBus from '../common/Eventbus'
export default {
    name: 'datepicker',
    data () {
        return {
            selectedDate: ""
        }
    },
    props: {
    },
    methods: {
        selectedValue () {
            let formattedValue = moment(String(this.selectedDate)).format("MM/DD/YYYY");
            eventBus.$emit('dateFilter', formattedValue)
        }
    }
}
</script>