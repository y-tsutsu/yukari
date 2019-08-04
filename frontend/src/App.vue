<template>
  <div id="app">
    <TopBar class="top-bar"></TopBar>
    <router-view></router-view>
  </div>
</template>

<script>
import TopBar from '@/components/TopBar.vue'

export default {
  name: 'app',
  components: {
    TopBar
  }
}
</script>

<style>
body {
  text-align: center;
}
.top-bar {
  margin-bottom: 30px
}
</style>
