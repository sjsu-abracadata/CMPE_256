<template>
  <div class="row">
    <div class="col-lg-9">
      <div class="row justify-content-center">
        <div class="col-md-6 col-lg-3">
          <div class="card report-card">
            <div class="card-body">
              <div class="row d-flex justify-content-center">
                <div class="col">
                  <p class="text-dark mb-0 fw-semibold">
                    Number of CNBC articles
                  </p>
                  <h3 class="m-0">{{ getcnbccount }}</h3>
                </div>
                <div class="col-auto align-self-center">
                  <div class="report-main-icon bg-light-alt">
                    <span
                      data-feather="users"
                      class="align-self-center text-muted icon-sm"
                      ><img
                        style="height: 52px;width: 52px;"
                        src="../../HTML/assets/images/brand-logo/cnbc.jpg"
                    /></span>
                  </div>
                </div>
              </div>
            </div>
            <!--end card-body-->
          </div>
          <!--end card-->
        </div>
        <!--end col-->
        <div class="col-md-6 col-lg-3">
          <div class="card report-card">
            <div class="card-body">
              <div class="row d-flex justify-content-center">
                <div class="col">
                  <p class="text-dark mb-0 fw-semibold">
                    Number of New York Times articles
                  </p>
                  <h3 class="m-0">{{ getnewyorkcount }}</h3>
                </div>
                <div class="col-auto align-self-center">
                  <div class="report-main-icon bg-light-alt">
                    <span
                      data-feather="users"
                      class="align-self-center text-muted icon-sm"
                      ><img
                        style="height: 52px;width: 52px;"
                        src="../../HTML/assets/images/brand-logo/ny.png"
                    /></span>
                  </div>
                </div>
              </div>
            </div>
            <!--end card-body-->
          </div>
          <!--end card-->
        </div>
        <!--end col-->
        <div class="col-md-6 col-lg-3">
          <div class="card report-card">
            <div class="card-body">
              <div class="row d-flex justify-content-center">
                <div class="col">
                  <p class="text-dark mb-0 fw-semibold">Bounce Rate</p>
                  <h3 class="m-0">$2400</h3>
                  <p class="mb-0 text-truncate text-muted">
                    <span class="text-danger"
                      ><i class="mdi mdi-trending-down"></i>35%</span
                    >
                    Bounce Rate Weekly
                  </p>
                </div>
                <div class="col-auto align-self-center">
                  <div class="report-main-icon bg-light-alt">
                    <i
                      data-feather="activity"
                      class="align-self-center text-muted icon-sm"
                    ></i>
                  </div>
                </div>
              </div>
            </div>
            <!--end card-body-->
          </div>
          <!--end card-->
        </div>
        <!--end col-->
        <div class="col-md-6 col-lg-3">
          <div class="card report-card">
            <div class="card-body">
              <div class="row d-flex justify-content-center">
                <div class="col">
                  <p class="text-dark mb-0 fw-semibold">Goal Completions</p>
                  <h3 class="m-0">85000</h3>
                  <p class="mb-0 text-truncate text-muted">
                    <span class="text-success"
                      ><i class="mdi mdi-trending-up"></i>10.5%</span
                    >
                    Completions Weekly
                  </p>
                </div>
                <div class="col-auto align-self-center">
                  <div class="report-main-icon bg-light-alt">
                    <i
                      data-feather="briefcase"
                      class="align-self-center text-muted icon-sm"
                    ></i>
                  </div>
                </div>
              </div>
            </div>
            <!--end card-body-->
          </div>
          <!--end card-->
        </div>
        <!--end col-->
      </div>
      <!--end row-->
      <div class="card">
        <div class="card-header">
          <div class="row align-items-center">
            <div class="col">
              <h4 class="card-title">Audience Overview</h4>
            </div>
            <!--end col-->
            <div class="col-auto">
              <div class="dropdown">
                <a
                  href="#"
                  class="btn btn-sm btn-outline-light dropdown-toggle"
                  data-bs-toggle="dropdown"
                  aria-haspopup="true"
                  aria-expanded="false"
                >
                  This Year<i class="las la-angle-down ms-1"></i>
                </a>
                <div class="dropdown-menu dropdown-menu-end">
                  <a class="dropdown-item" href="#">Today</a>
                  <a class="dropdown-item" href="#">Last Week</a>
                  <a class="dropdown-item" href="#">Last Month</a>
                  <a class="dropdown-item" href="#">This Year</a>
                </div>
              </div>
            </div>
            <!--end col-->
          </div>
          <!--end row-->
        </div>
        <!--end card-header-->
        <div class="card-body">
          <div class="">
            <apex-chart
              width="500"
              type="bar"
              :options="options"
              :series="series"
            ></apex-chart>
          </div>
        </div>
        <!--end card-body-->
      </div>
      <!--end card-->
    </div>
    <!--end col-->
    <div class="col-lg-3">
      <div class="card">
        <div class="card-header">
          <div class="row align-items-center">
            <div class="col">
              <h4 class="card-title">Sessions Device</h4>
            </div>
            <!--end col-->
            <div class="col-auto">
              <div class="dropdown">
                <a
                  href="#"
                  class="btn btn-sm btn-outline-light dropdown-toggle"
                  data-bs-toggle="dropdown"
                  aria-haspopup="true"
                  aria-expanded="false"
                >
                  All<i class="las la-angle-down ms-1"></i>
                </a>
                <div class="dropdown-menu dropdown-menu-end">
                  <a class="dropdown-item" href="#">Purchases</a>
                  <a class="dropdown-item" href="#">Emails</a>
                </div>
              </div>
            </div>
            <!--end col-->
          </div>
          <!--end row-->
        </div>
        <!--end card-header-->
        <div class="card-body">
          <div class="text-center">
            <div id="ana_device" class="apex-charts"></div>
            <h6 class="bg-light-alt py-3 px-2 mb-0">
              <i
                data-feather="calendar"
                class="align-self-center icon-xs me-1"
              ></i>
              01 January 2020 to 31 December 2020
            </h6>
          </div>
          <div class="table-responsive mt-2">
            <table class="table border-dashed mb-0">
              <thead>
                <tr>
                  <th>Device</th>
                  <th class="text-end">Sassions</th>
                  <th class="text-end">Day</th>
                  <th class="text-end">Week</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Dasktops</td>
                  <td class="text-end">1843</td>
                  <td class="text-end">-3</td>
                  <td class="text-end">-12</td>
                </tr>
                <tr>
                  <td>Tablets</td>
                  <td class="text-end">2543</td>
                  <td class="text-end">-5</td>
                  <td class="text-end">-2</td>
                </tr>
                <tr>
                  <td>Mobiles</td>
                  <td class="text-end">3654</td>
                  <td class="text-end">-5</td>
                  <td class="text-end">-6</td>
                </tr>
              </tbody>
            </table>
            <!--end /table-->
          </div>
          <!--end /div-->
        </div>
        <!--end card-body-->
      </div>
      <!--end card-->
    </div>
    <!--end col-->
  </div>
</template>

<script>
import ApexChart from "vue-apexcharts";
import axios from "axios";
export default {
  name: "dashboardcards",
  data() {
    return {
      options: {
        chart: {
          id: "vuechart-example",
        },
        xaxis: {
          categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998],
        },
      },
      series: [
        {
          name: "series-1",
          data: [30, 40, 45, 50, 49, 60, 70, 91],
        },
      ],
      cnbcArticlesCount: null,
      nyArticlesCount: null
    };
  },
  methods: {
    getcnbccountService() {
      axios.get("http://127.0.0.1:8000/cnbccount/").then(
        (response) => {
          this.cnbcArticlesCount = response.data;
        },
        (error) => {
          console.error(error);
        }
      );
      return this.cnbcArticlesCount;
    },
    getnewyorkcountService() {
      axios.get("http://127.0.0.1:8000/newyorktimescount/").then(
        (response) => {
          this.nyArticlesCount = response.data;
        },
        (error) => {
          console.error(error);
        }
      );
      return this.nyArticlesCount;
    },
  },
  computed: {
    getcnbccount() {
      return this.getcnbccountService();
    },
    getnewyorkcount() {
      return this.getnewyorkcountService();
    },
  },
  components: {
    ApexChart,
  },
};
</script>
