<template>
  <div class="home">
    <el-image class="main-image" src="/static/img/yuyushiki.jpg" fit="fill"></el-image>
    <el-table class="data-table" :data="tableData" stripe>
      <el-table-column prop="name" label="キャラクタ" width="180"></el-table-column>
      <el-table-column prop="cv" label="声優" width="180"></el-table-column>
      <el-table-column prop="note" label="性格"></el-table-column>
    </el-table>
  </div>
</template>

<script>
const axios = require('axios').create({ baseURL: 'http://127.0.0.1:5000' })

export default {
  name: 'home',
  data () {
    return {
      tableData: [],
      timer: null
    }
  },
  mounted () {
    this.updataTableData()
    this.timer = setInterval(this.updataTableData, 1000)
  },
  destroyed () {
    clearInterval(this.timer)
  },
  methods: {
    updataTableData: function () {
      axios.get('/api/infos').then(response => (this.tableData = response.data))
    }
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
