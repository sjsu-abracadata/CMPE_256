<template>
    <b-navbar  class="mb-4" :type="type" :variant="variant">
    <b-navbar-nav>
      <b-nav-item><h3 style="color:white;">{{message}}</h3></b-nav-item>
    </b-navbar-nav>
  </b-navbar>
</template>

<script>
export default {
    name: 'navbar',
    props: {
        message: String,
        type: String,
        variant: String
    }
}
</script>
