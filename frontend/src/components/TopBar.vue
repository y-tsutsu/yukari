<template>
  <div class="hello">
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      background-color="#7986cb"
      text-color="#fff"
      active-text-color="#fff59d"
    >
      <el-menu-item index="1">カメラ映像</el-menu-item>
      <el-menu-item>
        <a href="https://github.com/y-tsutsu/yukari" target="_blank">GitHub</a>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'TopBar',
  data () {
    return {
      activeIndex: '1'
    }
  }
}
</script>

<style scoped>
</style>
