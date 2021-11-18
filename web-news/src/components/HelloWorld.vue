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
        <button class="btn btn-primary" type="button" id="button-addon2">
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
        <Card
          :results="results"
          :per-page="perPage"
          :current-page="currentPage"
        />
      </div>
    </div>
  </div>
</template>


<script>
import Dropdown from "../common/Dropdown.vue";
import Card from "../common/Card.vue";
import Navbar from "../common/Navbar.vue";
import Datepicker from "../common/Datepicker.vue";
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
      results: [
        {
          headline: "255",
          body: "abc",
          url: "google.com",
          source: "CNBC",
          timestamp: "November 17, 2021 - 17:35:00",
        },
        {
          headline: "256",
          body: "xyz",
          url: "yahoo.com",
          source: "NY times",
          timestamp: "November 16, 2021 - 7:35:00",
        },
        {
          headline: "2564",
          body: "xyz",
          url: "yahoo.com",
          source: "NY times",
          timestamp: "November 16, 2021 - 7:35:00",
        },
        {
          headline: "25627",
          body: "xyz",
          url: "yahoo.com",
          source: "NY times",
          timestamp: "November 16, 2021 - 7:35:00",
        },
        {
          headline: "2565",
          body: "xyz",
          url: "yahoo.com",
          source: "NY times",
          timestamp: "November 16, 2021 - 7:35:00",
        },
        {
          headline: "2556",
          body: "xyz",
          url: "yahoo.com",
          source: "NY times",
          timestamp: "November 16, 2021 - 7:35:00",
        },
        {
          headline: "2656",
          body: "xyz",
          url: "yahoo.com",
          source: "NY times",
          timestamp: "November 16, 2021 - 7:35:00",
        },
        {
          headline: "3256",
          body: "xyz",
          url: "yahoo.com",
          source: "NY times",
          timestamp: "November 16, 2021 - 7:35:00",
        },
        {
          headline: "2567",
          body: "xyz",
          url: "yahoo.com",
          source: "NY times",
          timestamp: "November 16, 2021 - 7:35:00",
        },
        {
          headline: "2526",
          body: "xyz",
          url: "yahoo.com",
          source: "NY times",
          timestamp: "November 16, 2021 - 7:35:00",
        },
        {
          headline: "2536",
          body: "xyz",
          url: "yahoo.com",
          source: "NY times",
          timestamp: "November 16, 2021 - 7:35:00",
        },
        {
          headline: "2563",
          body: "xyz",
          url: "yahoo.com",
          source: "NY times",
          timestamp: "November 16, 2021 - 7:35:00",
        },
        {
          headline: "2561",
          body: "xyz",
          url: "yahoo.com",
          source: "NY times",
          timestamp: "November 16, 2021 - 7:35:00",
        },
        {
          headline: "223",
          body: "xyz",
          url: "yahoo.com",
          source: "NY times",
          timestamp: "November 16, 2021 - 7:35:00",
        },
        {
          headline: "276",
          body: "xyz",
          url: "yahoo.com",
          source: "NY times",
          timestamp: "November 16, 2021 - 7:35:00",
        },
      ],
    };
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
