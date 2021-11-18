<template>
  <div v-for="result in results" :key="result" class="col-sm-10 m-2">
    <div class="card">
      <!-- <div class="card-header float-start">{{ result.headline }}</div> -->
      <div class="card-body">
        <h5 class="card-title">
          <a target="_blank" class="float-start" :href="result.url">
            {{ result.headline }}
          </a>
        </h5>
        <br />
        <p class="card-text float-start">{{ result.body }}</p>
        <br />
        <hr />
        <div class="position-relative">
          <div class="position-absolute top-0 start-0">
            {{ result.source }}
          </div>
          <div class="position-absolute top-0 start-50">
            {{ result.timestamp }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  Name: "Card",
  props: {
    results: Array,
  },
  data() {
    return {};
  },
};
</script>

<style />