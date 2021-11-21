<template>
  <div>
    <Navbar message="CMPE 256 Abraca-Data" type="dark" variant="dark" />
    <div class="container">
      <div class="input-group mb-3">
        <input
          type="email"
          class="form-control"
          id="floatingInput"
          placeholder="Search"
          v-model="searchResult"
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
      <div class="form-check form-switch">
        <input
          class="form-check-input"
          type="checkbox"
          id="flexSwitchCheckDefault"
          v-model="switchValue"
          @change="showFiltersChange()"
        />
        <label
          class="form-check-label"
          style="display: flex"
          for="flexSwitchCheckDefault"
          >{{ checkSwitchValue }}</label
        >
      </div>
      <div v-if="showFilter">
        <div class="row">
          <div class="col-md-4 text-left">Search by Sources</div>
          <div class="col-md-4 text-left">Search by Authors</div>
          <div class="col-md-4 text-left">Search by Date</div>
        </div>
        <div class="row">
          <div class="col-md-4">
            <Dropdown :optionslist="source" :model="sourcesVal" @change="showVal()"/>
          </div>
          <div class="col-md-4">
            <Dropdown :optionslist="authors" />
          </div>
          <div class="col-md-4">
            <Datepicker />
          </div>
        </div>
      </div>
      <DashboardCards v-if="!showFilter"/>
      <div class="row" v-if="showFilter">
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
import DashboardCards from "../common/DashboardCards.vue";
import axios from "axios";
import eventBus from '../common/Eventbus'
import _ from 'lodash'
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
    DashboardCards,
  },
  data() {
    return {
      source: ["CNBC", "New York Times"],
      authors: ["Swathi", "Yash", "Aryan"],
      perPage: 5,
      currentPage: 1,
      results: [],
      switchValue: false,
      showFilter: false,
      searchResult: '',
      sourcesVal: '',
      originalResults: []
    };
  },
  methods: {
    showVal () {
      console.log(this.sourcesVal)
    },
    searchFilter () {
      axios.get(`http://127.0.0.1:8000/searchallrecords/${this.searchResult}`)
      .then(response => {
        this.results = response.data
        this.originalResults.push(...response.data)
      })
    },
    showFiltersChange() {
      this.showFilter = this.switchValue;
    },
    getcnbcdata() {
      axios.get("http://127.0.0.1:8000/cnbc/").then(
        (response) => {
          this.results.push(...response.data);
        },
        (error) => {
          console.error(error);
        }
      );
    },
    getnytimesdata() {
      axios.get("http://127.0.0.1:8000/newyorktimes/").then(
        (response) => {
          this.results.push(...response.data);
        },
        (error) => {
          console.error(error);
        }
      );
    },
    filterSource (value) {
      this.results = this.originalResults
      if(value === 'CNBC') this.results = _.filter(this.results, {'source': 'CNBC'})
      else this.results = _.filter(this.resullts, {'source': 'Newyork Times'})
    }
  },
  mounted() {
    eventBus.$on('modelVal', (value)=>{
      this.sourcesVal = value
      if(this.sourcesVal === 'CNBC') {
        this.filterSource('CNBC')
      } else {
        this.filterSource('NY')
      }
    })
  },
  computed: {
    checkSwitchValue() {
      return this.switchValue ? "Show Dashboard" : "Hide Dashboard and show filters";
    },
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
