# Yukari -- 縁 --

Networkカメラなどの映像に対して画像処理を行い，その結果加工した映像や情報をリアルタイムにブラウザ上に表示するWebアプリのデモ．

# 実行環境（開発環境）のセットアップ

## Git Clone

```sh
$ git clone https://github.com/y-tsutsu/yukari.git
```

## フロントエンド

Vue.js + Element を使ったフロントエンドの環境構築

### Requirements

* Node.js (20.9)
* npm (9.5)

### Install

関連パッケージをインストール

```sh
$ cd ./yukari/frontend
$ npm ci
$ npm run download-fonts
```

### Build

バックエンド側から読み込む一式を生成する

```sh
$ cd ./yukari/frontend
$ npm run build  # Output dist directory
```

## バックエンド

Flask を使ったバックエンド（Webサーバ SPA・REST）の環境構築  
OpenCVを使った画像認識の環境構築

### Requirements

* Python (3.12)
* pip (23.3)
* pipenv (2023.11.15)

### Install

関連パッケージをインストール

```sh
$ cd ./yukari/backend
$ pipenv sync        # 実行環境の場合
$ pipenv sync --dev  # 開発環境の場合
```

# 実行手順

## フロントエンド

フロントエンド単体の開発用サーバを起動

### Run Dev Server

フロントエンドの開発用のDummy REST Serverの起動

```sh
$ cd ./yukari/frontend
$ npm run json-mock
```

フロントエンドの開発用サーバの起動

```sh
$ cd ./yukari/frontend
$ npm run serve  # Access to http://localhost:8080/
```

## バックエンド

本番環境のWebサーバの起動

### Run Server

フロントエンドのWebサーバの起動（事前にフロントエンドのBuildが必要）

```sh
$ cd ./yukari/backend
$ pipenv run start  # Access to http://localhost/
```
