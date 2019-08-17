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
  },
  methods: {
    createPageTitle: function (to) {
      if (to.meta.title) {
        var setTitle = 'Yukari | ' + to.meta.title
        document.title = setTitle
      } else {
        document.title = 'Yukari'
      }
    }
  },
  mounted: function () {
    var to = this.$route
    this.createPageTitle(to)
  },
  watch: {
    '$route' (to, from) {
      this.createPageTitle(to)
    }
  }
}
</script>

<style scoped>
#app {
  font-family: 'M PLUS 1p', 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
}
.top-bar {
  margin-bottom: 30px
}
</style>
