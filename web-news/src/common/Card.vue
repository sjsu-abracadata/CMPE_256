<template>
  <div class="col-sm-12">
    <div class="card" v-for="item in paginatedItems" :key="item.url">
      <div class="card-body">
        <div class="text-center">
          <img
            v-if="item.source === 'CNBC'"
            class="m-3 rounded-circle thumb-xl"
            src="../../HTML/assets/images/brand-logo/cnbc.jpg"
            alt=""
          />
          <img
            v-else-if="item.source === 'Newyork Times'"
            class="m-3 rounded-circle thumb-xl"
            src="../../HTML/assets/images/brand-logo/ny.png"
            alt=""
          />
          <div class="">
            <small class="text-muted"
              ><a target="_blank" :href="item.url">
                {{ item.headline }}
              </a>
            </small>
          </div>
          <a
            href="#"
            class="me-3 text-warning"
            v-for="authors in item.authors"
            :key="authors"
            >{{ authors }} <span>&#183;</span></a
          >
          <p class="text-muted px-3">
            {{ item.body }}
          </p>
          <div class="mb-3">
            <a href="#" class="me-3 text-warning">{{
              item.published_timestamp | formatDate
            }}</a>
            <a href="#" class="me-3 text-warning">2843 Followers</a>
            <a href="#" class="text-warning">295 Following</a>
          </div>
          <button type="button" class="btn btn-sm btn-soft-primary">
            More Detail
          </button>
        </div>
      </div>
      <!--end card-body-->
    </div>
    <b-pagination
      @change="onPageChanged"
      :total-rows="totalRows"
      :per-page="perPage"
      v-model="currentPage"
      class="my-0"
      v-if="results.length"
    ></b-pagination>
  </div>
</template>

<script>
import moment from "moment";
export default {
  Name: "Card",
  props: {
    results: Array,
  },
  filters: {
    formatDate(value) {
      return moment(String(value)).format("MM/DD/YYYY");
    },
  },
  component: {},
  data() {
    return {
      resultValues: [],
      paginatedItems: this.results,
      perPage: 3,
      totalRows: this.results.length,
      currentPage: 1,
    };
  },
  watch: {
    results() {
      this.paginatedItems = this.results;
      this.totalRows = this.results.length
    },
  },
  computed: {
    pageCount() {
      let l = this.totalRows,
        s = this.perPage;
      return Math.floor(l / s);
    },
  },
  mounted() {
    this.paginate(this.perPage, 0);
  },
  methods: {
    paginate(page_size, page_number) {
      let itemsToParse = this.results;
      this.paginatedItems = itemsToParse.slice(
        page_number * page_size,
        (page_number + 1) * page_size
      );
    },
    onPageChanged(page) {
      this.paginate(this.perPage, page - 1);
    },
  },
};
</script>

<style />