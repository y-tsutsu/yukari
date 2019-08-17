<template>
  <div class="hello">
    <el-menu
      :default-active="activeIndex"
      mode="horizontal"
      background-color="#7986cb"
      text-color="#fff"
      active-text-color="#fff59d"
      router
    >
      <el-menu-item index="home" :route="{ name:'home' }">カメラ映像</el-menu-item>
      <el-menu-item index="about" :route="{ name:'about' }">アバウト</el-menu-item>
      <el-menu-item>
        <a href="https://github.com/y-tsutsu/yukari" target="_blank" class="a-link">GitHub</a>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'TopBar',
  data () {
    return {
      activeIndex: this.$route.name
    }
  }
}
</script>

<style scoped>
.a-link {
  text-decoration: none;
}
</style>
