<template>
  <div>
    <div class="input-group" v-if="type === 'source'">
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
    <div class="input-group" v-if="type === 'authors'">
      <select
        class="form-select"
        id="inputGroupSelect04"
        aria-label="Example select with button addon"
        v-model="modelValAuthors"
        @change="emitValueAuth()"
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
    model: String,
    type: String,
    modelValAuth: String
  },
  methods: {
    emitValue () {
      eventBus.$emit('modelVal', this.modelVal)
    },
    emitValueAuth () {
      eventBus.$emit('modelValAuthors', this.modelValAuthors)
    }
  },
  data() {
    return {
      modelVal: this.model,
      modelValAuthors: this.modelValAuth
    };
  },
  watch: {
    model () {
      this.modelVal = this.model
    },
    modelValAuth () {
      this.modelValAuthors = this.modelValAuth
    }
  }
};
</script>

<style>
</style>