<template>
  <div class="home">
    <el-image v-if="usedSampleImage" class="main-image" src="/static/img/yuyushiki.jpg" fit="fill"></el-image>
    <el-image v-else class="main-image" src="/video" fit="fill"></el-image>

    <el-table class="data-table" :data="tableData" stripe>
      <el-table-column prop="name" label="キャラクタ" width="180"></el-table-column>
      <el-table-column prop="cv" label="声優" width="180"></el-table-column>
      <el-table-column prop="note" label="性格"></el-table-column>
      <el-table-column prop="pos" label="位置" width="120"></el-table-column>
    </el-table>
  </div>
</template>

<script>
const axios =
  process.env.VUE_APP_REST_SERVER === 'json-mock'
    ? require('axios').create({ baseURL: 'http://localhost:5000' })
    : require('axios')

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
    this.timer = setInterval(this.updataTableData, 500)
  },
  destroyed () {
    clearInterval(this.timer)
  },
  methods: {
    updataTableData: async function () {
      const response = await axios.get('/api/infos')
      this.tableData = response.data
    }
  },
  computed: {
    usedSampleImage () {
      return process.env.VUE_APP_SAMPLE_IMAGE
    }
  }
}
</script>

<style scoped>
.main-image {
  margin-bottom: 30px;
  width: 45%;
}
.data-table {
  width: 60%;
  margin: auto;
}
</style>
