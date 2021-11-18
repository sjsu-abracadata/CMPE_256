<template>
  <div class="col-sm-10 m-2">
    <div class="card" v-for="(item, index) in paginatedItems" :key="index">
      <!-- <div class="card-header float-start">{{ result.headline }}</div> -->
      <div class="card-body">
        <h5 class="card-title">
          <a target="_blank" class="float-start" :href="item.url">
            {{ item.headline }}
          </a>
        </h5>
        <br />
        <p class="card-text float-start">{{ item.body }}</p>
        <br />
        <hr />
        <div class="row">
          <div class="col-sm-6">
            {{ item.source }}
          </div>
          <div class="col-sm-6">
            {{ item.timestamp }}
          </div>
        </div>
      </div>
    </div>

    <b-pagination
       @change="onPageChanged" :total-rows="totalRows" :per-page="perPage" v-model="currentPage" class="my-0"
    ></b-pagination>
  </div>
</template>

<script>
export default {
  Name: "Card",
  props: {
    results: Array
  },
  component: {
  },
  data() {
    return {
      resultValues: [],
      paginatedItems: this.results,
      perPage: 4,
      totalRows: this.results.length,
      currentPage: 1
    };
  },
  watch: {
    results() {
      this.paginatedItems = this.results
    }
  },
  computed: {
    pageCount() {
      let l = this.totalRows,
        s = this.perPage;
      return Math.floor(l / s);
    }
  },
  mounted(){
    this.paginate(this.perPage, 0)
  },
  methods: {
    paginate (page_size, page_number) {
      let itemsToParse = this.results
      this.paginatedItems = itemsToParse.slice(page_number * page_size, (page_number + 1) * page_size);
    },
    onPageChanged(page){
      this.paginate(this.perPage, page - 1)
    }
  }
};
</script>

<style />