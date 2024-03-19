{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM8q5kkNBWCulhQfp6pHaBe",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Haiderr23/Haider-Santiago-Calderon-Rodriguez/blob/main/2024_0315_Estadisticos.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hN4-qaKKjlNG",
        "outputId": "b3ae36da-5dc3-4e22-84cf-7589295a47a0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Promedio: 40.0\n",
            "Desviacion estandar: 7.0710678118654755\n",
            "Varianza: 50.0\n"
          ]
        }
      ],
      "source": [
        "#Haider Santiago Calderón Rodríguez 20211005075\n",
        "from math import sqrt\n",
        "\n",
        "v = [45, 50, 30, 40, 35]\n",
        "\n",
        "def promedio(v):\n",
        "    k = len(v)\n",
        "    x = 0\n",
        "    for i in range(k):\n",
        "        x += v[i]\n",
        "    prom = x / k\n",
        "    return prom\n",
        "\n",
        "print(\"Promedio:\",promedio(v))\n",
        "\n",
        "def desv_est(v):\n",
        "    k = len(v)\n",
        "    prom = promedio(v)\n",
        "    x = 0\n",
        "    for i in range(k):\n",
        "        x += (v[i] - prom)**2\n",
        "    desv_est = sqrt(x / k)\n",
        "    return desv_est\n",
        "\n",
        "print(\"Desviacion estandar:\",desv_est(v))\n",
        "\n",
        "def varianza(v):\n",
        "    k = len(v)\n",
        "    prom = promedio(v)\n",
        "    x = 0\n",
        "    for i in range(k):\n",
        "        x += (v[i] - prom)**2\n",
        "    vari = (x / k)\n",
        "    return vari\n",
        "\n",
        "print(\"Varianza:\",varianza(v))"
      ]
    }
  ]
}