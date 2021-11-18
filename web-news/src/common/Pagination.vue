<template>
  <nav aria-label="Page navigation example">
    <ul class="pagination">
      <li
        class="page-item"
        v-for="(pages, index) in result.length"
        :key="index"
      >
        <a class="page-link" href="#">{{ index + 1 }}</a>
      </li>
    </ul>
  </nav>
</template>
<script>
export default {
  name: "Pagination",
  component: {},
  props: {
    result: Array,
  },
};
</script>