<template>
  <div>
    <div class="input-group">
      <select
        class="form-select"
        id="inputGroupSelect04"
        aria-label="Example select with button addon"
        v-model="modelVal"
        @change="emitValue()"
      >
        <option>Select</option>
        <option v-for="(options) in optionslist" :key="options">
          {{ options }}
        </option>
      </select>
    </div>
  </div>
</template>

<script>
import eventBus from '../common/Eventbus'
export default {
  Name: "Dropdown",
  props: {
    optionslist: Array,
    model: String
  },
  methods: {
    emitValue () {
      eventBus.$emit('modelVal', this.modelVal)
    }
  },
  data() {
    return {
      modelVal: this.model
    };
  },
  watch: {
    model () {
      this.modelVal = this.model
    }
  }
};
</script>

<style>
</style>