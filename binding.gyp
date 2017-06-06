{
  'targets': [
    {
      'target_name': 'speaker',
      'sources': [
        'src/binding.cc',
      ],
      "include_dirs" : [
        '<!(node -e "require(\'nan\')")'
      ],
      'dependencies': [
        'deps/mpg123/mpg123.gyp:output'
      ],
    }
  ]
}
