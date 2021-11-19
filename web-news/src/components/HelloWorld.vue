<template>
  <div>
    <Navbar message="CMPE 256 Abraca-Data" type="dark" variant="dark" />
    <div class="container">
      <div class="input-group mb-3">
        <input
          type="text"
          class="form-control"
          placeholder="Please enter author name or article title to start searching"
          aria-label="Recipient's username"
          aria-describedby="button-addon2"
        />
        <button
          class="btn btn-primary"
          type="button"
          id="button-addon2"
          @click="searchFilter()"
        >
          Search
        </button>
      </div>

      <div class="row">
        <div class="col-md-4 text-left">Search by Authors</div>
        <div class="col-md-4 text-left">Search by Sources</div>
        <div class="col-md-4 text-left">Search by Date</div>
      </div>
      <div class="row">
        <div class="col-md-4">
          <Dropdown :optionslist="source" />
        </div>
        <div class="col-md-4">
          <Dropdown :optionslist="authors" />
        </div>
        <div class="col-md-4">
          <Datepicker />
        </div>
      </div>
      <div class="row">
        <Card :results="results" />
      </div>
    </div>
  </div>
</template>


<script>
import Dropdown from "../common/Dropdown.vue";
import Card from "../common/Card.vue";
import Navbar from "../common/Navbar.vue";
import Datepicker from "../common/Datepicker.vue";
import axios from "axios";
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
  components: {
    Dropdown,
    Card,
    Navbar,
    Datepicker,
  },
  data() {
    return {
      source: ["CNBC", "New York Times"],
      authors: ["Swathi", "Yash", "Aryan"],
      perPage: 5,
      currentPage: 1,
      results: [],
    };
  },
  methods: {
    searchFilter() {},
  },
  mounted() {
    axios.get("http://127.0.0.1:8000/cnbc/").then(
      (response) => {
        console.log(response);
        this.results = response.data;
      },
      (error) => {
        console.error(error);
      }
    );
  },
};
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
.text-left {
  text-align: start;
}
</style>
