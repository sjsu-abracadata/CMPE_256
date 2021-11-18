<template>
    <div>
        <div class="input-group">
          <select class="form-select" id="inputGroupSelect04" aria-label="Example select with button addon">
              <option v-for="options in optionslist" :key="options">{{options}}</option>
          </select>
        </div>
    </div>
</template>

<script>
export default {
    Name: 'Dropdown',
    props: {
        optionslist: Array
    },
    data () {
        return {
        } 
    }
}
</script>

<style>

</style>