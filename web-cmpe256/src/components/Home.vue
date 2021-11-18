<template>
  <div class="container">
    <div class="input-group mb-3">
      <input type="text" class="form-control" placeholder="Recipient's username" aria-label="Recipient's username" aria-describedby="button-addon2">
      <button class="btn btn-outline-secondary" type="button" id="button-addon2">Button</button>
    </div>
    <div class="row">
      <div class="col-md-4">
        <Dropdown :optionslist="source"/>
      </div>
      <div class="col-md-4">
        <Dropdown :optionslist="authors"/>
      </div>
      <div class="col-md-4">
        <div id="date-picker-example" class="md-form md-outline input-with-post-icon datepicker">
        <input placeholder="Select date" type="text" id="example" class="form-control">
        <label for="example">Try me...</label>
        <i class="fas fa-calendar input-prefix" tabindex=0></i>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
import Dropdown from './common/Dropdown.vue'
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  components: {
    Dropdown
  },
  data () {
    return {
      source: ['CNBC', 'New York Times'],
      authors: ['Swathi', 'Yash', 'Aryan']
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
