<template>
  <div class="home">
    <el-image
      class="main-image"
      src="http://news.denfaminicogamer.jp/wp-content/uploads/2017/03/yu3.jpg"
      fit="fill"
    ></el-image>
    <el-table class="data-table" :data="tableData" stripe>
      <el-table-column prop="name" label="キャラクタ" width="180"></el-table-column>
      <el-table-column prop="cv" label="声優" width="180"></el-table-column>
      <el-table-column prop="note" label="性格"></el-table-column>
    </el-table>
  </div>
</template>

<script>
const axios = require('axios');

export default {
  name: 'home',
  data () {
    return {
      tableData: []
    }
  },
  mounted () {
    axios.get('/api/infos').then(response => (this.tableData = response.data))
  }
}
</script>

<style scoped>
.main-image {
  margin-bottom: 30px;
}
.data-table {
  width: 60%;
  margin: auto;
}
</style>
