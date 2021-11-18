<template>
  <div class="container">
    <div class="input-group mb-3">
      <input
        type="text"
        class="form-control"
        placeholder="Recipient's username"
        aria-label="Recipient's username"
        aria-describedby="button-addon2"
      />
      <button
        class="btn btn-outline-secondary"
        type="button"
        id="button-addon2"
      >
        Button
      </button>
    </div>
    <div class="row">
      <div class="col-md-4">
        <Dropdown :optionslist="source" />
      </div>
      <div class="col-md-4">
        <Dropdown :optionslist="authors" />
      </div>
      <div class="col-md-4">
        <div
          id="date-picker-example"
          class="md-form md-outline input-with-post-icon datepicker"
        >
          <input
            placeholder="Select date"
            type="text"
            id="example"
            class="form-control"
          />
          <label for="example">Try me...</label>
          <i class="fas fa-calendar input-prefix" tabindex="0"></i>
        </div>
      </div>
    </div>
    <div class="row">
      <Card :results="results" 
      :per-page="perPage"
      :current-page="currentPage"/>
    </div>
  </div>
</template>


<script>
import Dropdown from "../common/Dropdown.vue";
import Card from "../common/Card.vue";

export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
  components: {
    Dropdown,
    Card
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
</style>
