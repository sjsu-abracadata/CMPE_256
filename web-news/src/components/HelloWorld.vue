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
            <Dropdown :optionslist="source" :model="sourcesVal" type="source"/>
          </div>
          <div class="col-md-4">
            <Dropdown
              :optionslist="authors"
              :model="authorsval"
              type="authors"
            />
          </div>
          <div class="col-md-4">
            <Datepicker />
          </div>
        </div>
      </div>
      <DashboardCards v-if="!showFilter" />
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
import eventBus from "../common/Eventbus";
import _ from "lodash";
import moment from "moment";
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
      source: ["CNBC", "Newyork Times"],
      authors: [],
      perPage: 5,
      currentPage: 1,
      results: [],
      switchValue: false,
      showFilter: false,
      searchResult: "",
      sourcesVal: "",
      originalResults: [],
      authorsval: "",
    };
  },
  methods: {
    showVal() {
      console.log(this.sourcesVal);
    },
    searchFilter() {
      axios
        .get(`http://127.0.0.1:8000/searchallrecords/${this.searchResult}`)
        .then((response) => {
          _.forEach(response.data, (value) => {
            this.authors.push(...value.authors);
            this.authors = _.uniq(this.authors);
          });
          this.results = response.data;
          this.originalResults = response.data;
          this.switchValue = true;
          this.showFilter = true;
        });
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
    filterSource(value) {
      this.results = this.originalResults;
      if (value === "CNBC") {
        this.results = _.filter(this.results, { source: "CNBC" });
        let author = [];
        _.forEach(this.results, (value) => {
          author.push(...value.authors);
        });
        this.authors = author;
        this.authors = _.uniq(this.authors);
      } else if (value === "NY")
        this.results = _.filter(this.results, { source: "Newyork Times" });
    },
    filterAuth() {
      let dummy = [];
      if (this.sourcesVal) {
        _.forEach(this.originalResults, (value) => {
          if (_.includes(value.authors, this.authorsval)) {
            dummy.push(value);
          }
        });
      }
      this.results = dummy;
    },
    filterDate(valueReturn) {
      let dummy = [];
      _.forEach(this.originalResults, (value) => {
        let formattedValue = moment(String(value.published_timestamp)).format(
          "MM/DD/YYYY"
        );
        if (formattedValue === valueReturn) {
          dummy.push(value);
        }
      });
      this.results = dummy;
    },
  },
  mounted() {
    eventBus.$on("modelVal", (value) => {
      this.sourcesVal = value;
      if (value === "CNBC") {
        this.filterSource("CNBC");
      } else if (value === "Newyork Times") {
        this.filterSource("NY");
      }
    });
    eventBus.$on("modelValAuthors", (value) => {
      this.authorsval = value;
      this.filterAuth();
    });
    eventBus.$on("dateFilter", (value) => {
      this.filterDate(value);
    });
  },
  computed: {
    checkSwitchValue() {
      return this.switchValue
        ? "Show Dashboard"
        : "Hide Dashboard and show filters";
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
