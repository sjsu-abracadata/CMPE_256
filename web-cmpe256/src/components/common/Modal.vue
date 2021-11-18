<template>
  <div>
    {{ message }}
  </div>
</template>
<script>
export default {
  name: "modal",
  data() {
    return {};
  },
  props: {
    message: String,
  },
};
</script>
